---
title: "Jekyll 블로그에 태그 시스템 추가하기"
categories: github-blog
tags: ['jekyll']
---

Jekyll 블로그에 태그 시스템을 추가하는 방법을 단계별로 설명하겠습니다. 이 가이드를 따라하면 블로그 포스트를 태그로 분류하고, 태그별 페이지를 자동으로 생성할 수 있습니다.

## Jekyll 블로그의 태그 시스템 원리 이해하기

Jekyll은 정적 사이트 생성기로, 마크다운 파일을 HTML로 변환하여 웹사이트를 만듭니다. 태그 시스템은 이러한 Jekyll의 작동 방식을 활용하여 구현됩니다.

### 1. 태그 데이터 수집
- Jekyll은 각 포스트의 Front Matter에서 태그 정보를 읽어들입니다.
- 이 정보는 `site.tags`라는 전역 변수에 저장되며, 각 태그별로 관련 포스트들이 자동으로 그룹화됩니다.
- Front Matter의 tags 필드는 YAML 배열 형식으로 작성되며, Jekyll이 빌드 시점에 이를 파싱합니다.

### 2. 태그 페이지 생성 과정
- `_plugins`폴더에 `tag_generator.rb` 파일을 생성한다.
- `tag_generator.rb` 플러그인은 사이트가 빌드될 때 실행됩니다.
- 포스트에서 사용된 모든 태그를 감지하고, 각 태그별로 별도의 페이지를 자동 생성합니다.
- 생성된 페이지는 Jekyll의 페이지 생성 파이프라인을 통해 처리됩니다.
- 이 과정에서 Liquid 템플릿 엔진이 동적으로 태그별 포스트 목록을 생성합니다.

### 3. 레이아웃과 템플릿 시스템
- Jekyll의 Liquid 템플릿 엔진을 사용하여 태그 페이지를 동적으로 구성합니다.
- `{% raw %}{% for %}{% endraw %}` 등의 Liquid 태그로 태그별 포스트 목록을 생성합니다.
- 이는 빌드 시점에 실행되어 정적 HTML로 변환됩니다.
- 레이아웃 파일은 재사용 가능한 템플릿을 제공하여 일관된 디자인을 유지합니다.

### 4. 사이드바와의 통합
- `_data/navigation.yml`의 구조는 Jekyll의 데이터 파일 시스템을 활용합니다.
- 이 데이터는 `site.data.navigation`으로 접근할 수 있으며, 템플릿에서 동적으로 메뉴를 생성하는 데 사용됩니다.
- YAML 형식의 데이터 파일은 Jekyll이 빌드할 때 자동으로 로드되어 전역 변수로 사용됩니다.

이러한 방식으로 Jekyll은 정적 사이트임에도 불구하고, 동적인 태그 시스템을 구현할 수 있습니다. 모든 처리는 빌드 시점에 이루어지므로, 실제 서비스되는 웹사이트는 빠르고 안정적으로 동작합니다.

## 1. 태그 페이지 생성하기

먼저 태그 목록을 보여줄 메인 페이지를 생성합니다.

`/tags/index.html` 파일을 생성하고 다음 내용을 추가합니다:

```html
---
layout: default
title: Tags
author_profile: true
sidebar:
  nav: "categories"
---

<div id="main" role="main">
  {% raw %}{% include sidebar.html %}{% endraw %}

  <div class="archive">
    <h1 class="page__title">{{ page.title }}</h1>
    
    {% raw %}{% capture site_tags %}{% for tag in site.tags %}{{ tag | first }}{% unless forloop.last %},{% endunless %}{% endfor %}{% endcapture %}
    {% assign tags_list = site_tags | split:',' | sort %}

    <div class="entries-{{ entries_layout | default: 'list' }}">
      {% for item in (0..site.tags.size) %}{% unless forloop.last %}
        {% capture this_tag %}{{ tags_list[item] | strip_newlines }}{% endcapture %}
        <div class="tag-group">
          <h2 id="{{ this_tag }}" class="archive__subtitle">{{ this_tag }}</h2>
          {% for post in site.tags[this_tag] %}
            <div class="list__item">
              <article class="archive__item">
                <h3 class="archive__item-title no_toc">
                  <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
                </h3>
                <p class="archive__item-excerpt">
                  <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%Y-%m-%d" }}</time>
                </p>
              </article>
            </div>
          {% endfor %}
        </div>
      {% endunless %}{% endfor %}{% endraw %}
    </div>
  </div>
</div>
```

## 2. 태그 레이아웃 생성하기

개별 태그 페이지의 레이아웃을 정의하기 위해 `/_layouts/tag.html` 파일을 생성합니다:

```html
---
layout: archive
---

{{ content }}

<div class="entries-{{ entries_layout | default: 'list' }}">
  {% raw %}{% for post in site.tags[page.tag] %}
    {% include archive-single.html %}
  {% endfor %}{% endraw %}
</div>
```

## 3. 태그 자동 생성 플러그인 추가하기

태그별 페이지를 자동으로 생성하기 위한 플러그인을 추가합니다. `/_plugins/tag_generator.rb` 파일을 생성하고 다음 내용을 추가합니다:

```ruby
Jekyll::Hooks.register :posts, :post_write do |post|
  all_existing_tags = Dir.entries("_tags")
    .map { |t| t.match(/(.*).md/) }
    .compact.map { |m| m[1] }

  tags = post['tags'].reject { |t| t.empty? }
  tags.each do |tag|
    generate_tag_file(tag) if !all_existing_tags.include?(tag)
  end
end

def generate_tag_file(tag)
  File.open("_tags/#{tag}.md", "wb") do |file|
    file << "---\nlayout: tag\ntag: #{tag}\n---\n"
  end
end
```

## 4. 포스트에 태그 추가하기

이제 블로그 포스트의 Front Matter에 태그를 추가할 수 있습니다:

```yaml
---
title: "포스트 제목"
categories: category-name
tags:
  - Tag1
  - Tag2
  - Tag3
---
```

## 5. 사이드바에 카테고리 메뉴 추가하기

`/_data/navigation.yml` 파일에 카테고리 네비게이션을 추가합니다:

```yaml
# sidebar navigation
categories:
  - title: Programming
    children:
      - title: "Data Structure and Algorithm" 
        url: /datastructure-and-algorithm/
      - title: "Python 기본 문법"
        url: /python-basic/
  - title: AI
    children:
      - title: "Machine Learning"
        url: /machine-learning/
  # 필요한 만큼 카테고리 추가
```

## 주의사항

1. GitHub Pages에서는 커스텀 플러그인을 지원하지 않습니다. 로컬에서 사이트를 빌드한 후 결과물을 푸시하거나, GitHub Actions를 사용해야 합니다.
2. 태그 이름에는 공백 대신 하이픈(-)을 사용하는 것이 좋습니다.

## 결과

이제 블로그에서 다음과 같은 기능을 사용할 수 있습니다:

- `/tags` 페이지에서 모든 태그와 관련 포스트 목록 확인
- 각 태그별 전용 페이지 자동 생성
- 사이드바에서 카테고리별 포스트 쉽게 탐색