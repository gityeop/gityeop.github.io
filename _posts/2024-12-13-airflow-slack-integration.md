# Airflow와 Slack 연동하기: 작업 실패 알림 구현하기

## 소개

Apache Airflow에서 작업이 실패할 때 Slack으로 알림을 받는 방법을 알아본다. 이는 데이터 파이프라인 모니터링에 매우 유용한 기능이다.

## 필요한 패키지

- Apache Airflow
- Slack Webhook URL

## 구현 방법

### 1. Slack Webhook 설정

먼저 Slack에서 Incoming Webhook을 설정해야 한다. 이는 Slack 워크스페이스의 설정에서 할 수 있다.
![Image](https://i.imgur.com/nfpAi86.png)
![Image](https://i.imgur.com/rxfa7tb.png)
![Image](https://i.imgur.com/JtvjLC2.png)
![Image](https://i.imgur.com/sbAwZP4.png)

### 2. Slack 알림 함수 구현

```python
def task_fail_slack_alert(context):
    slack_msg = f"""
        :red_circle: Task Failed.
        *Task*: {context.get('task_instance').task_id}
        *Dag*: {context.get('task_instance').dag_id}
        *Execution Time*: {context.get('execution_date')}
        *Log Url*: {context.get('task_instance').log_url}
        """
    # Slack webhook을 통해 메시지 전송
```

### 3. DAG 설정

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from airflow.exceptions import AirflowFailException

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# 데이터 처리 함수 예시
def process_data():
    # 데이터 처리 로직
    # 실패 시 예외 발생
    raise AirflowFailException("데이터 처리 중 오류 발생")

# 데이터 검증 함수 예시
def validate_data():
    # 데이터 검증 로직
    pass

with DAG(
    dag_id='example_data_pipeline',
    default_args=default_args,
    schedule_interval="0 */6 * * *",  # 6시간마다 실행
    catchup=False,
    tags=['example'],
    on_failure_callback=task_fail_slack_alert,
) as dag:
    
    # 데이터 처리 태스크
    process_task = PythonOperator(
        task_id='process_data',
        python_callable=process_data
    )
    
    # 데이터 검증 태스크
    validate_task = PythonOperator(
        task_id='validate_data',
        python_callable=validate_data
    )
    
    process_task >> validate_task
```

## 주요 포인트

1. `on_failure_callback`을 DAG 레벨에서 설정하면 모든 태스크의 실패를 감지할 수 있다
2. 각 태스크별로 다른 알림 설정이 필요한 경우, 태스크 레벨에서 개별적으로 설정할 수 있다
3. Slack 메시지에 포함되는 정보는 커스터마이징이 가능하다 (예: 에러 메시지, 재시도 횟수 등)

## 활용 사례

1. **데이터 수집 모니터링**
   - 외부 API에서 데이터 수집 실패 시 알림
   - 데이터베이스 연결 오류 감지

2. **ETL 파이프라인 관리**
   - 데이터 변환 작업 실패 알림
   - 데이터 적재 오류 감지

3. **시스템 헬스체크**
   - 주기적인 시스템 점검 결과 알림
   - 리소스 사용량 임계치 초과 알림

## 결론

Airflow와 Slack의 연동은 데이터 파이프라인 관리를 더욱 효율적으로 만든다. 실시간으로 작업 실패를 감지하고 빠른 대응이 가능하며, 다양한 모니터링 시나리오에 적용할 수 있다.
