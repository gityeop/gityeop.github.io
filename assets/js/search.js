document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.querySelector('.search-input');
    const searchContent = document.querySelector('.search-content__inner-wrap');
    const searchContainer = document.querySelector('.search-content');
  
    let idx = null;
    let data = [];
  
    // search-data.json 로드 (jekyll 빌드시 검색 인덱스용 json 자동 생성 후 사용)
    fetch('{{ site.baseurl }}/search-data.json')
      .then(response => response.json())
      .then(json => {
        data = json;
        idx = lunr(function () {
          this.ref('url');
          this.field('title');
          this.field('content');
          json.forEach(doc => this.add(doc));
        });
      });
  
    searchInput.addEventListener('input', function() {
      const query = this.value.trim();
      if (!query) {
        // 입력 없으면 숨기기
        searchContainer.classList.add('hidden');
        searchContent.innerHTML = '';
        return;
      }
  
      // 검색 실행
      const results = idx.search(query);
      searchContent.innerHTML = ''; 
      if (results.length > 0) {
        results.forEach(result => {
          const item = data.find(d => d.url === result.ref);
          if (item) {
            searchContent.innerHTML += `<div><a href="${item.url}">${item.title}</a></div>`;
          }
        });
        // 결과 있으면 표시
        searchContainer.classList.remove('hidden');
      } else {
        // 결과 없으면 숨기기
        searchContainer.classList.add('hidden');
      }
    });
  });
  