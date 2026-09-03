---
type: Reference
title: Open Knowledge Format (OKF)
description: 사람과 AI 에이전트가 함께 읽고 쓰는 경량 지식 문서 규약이에요.
tags: [knowledge, okf, documentation, standard]
---

# Open Knowledge Format (OKF)

OKF(Open Knowledge Format)는 사람과 AI 에이전트가 함께 지식을 기록하고 공유하기 위한 경량 마크다운 문서 규약이에요.

별도의 복잡한 도구나 데이터베이스 없이 Git 저장소 안에서 마크다운과 YAML 프론트매터만으로 지식을 관리할 수 있어요.

## 1. 기본 원칙

- **단일 주제 원칙**: 문서 하나는 하나의 명확한 개념이나 규칙만 다뤄요.
- **사람과 에이전트 친화성**: 사람은 마크다운 문서로 편하게 읽고, AI 에이전트는 YAML 메타데이터로 정확하게 파싱해요.
- **구조화된 본문**: 서술형 줄글보다는 제목, 번호 목록, 표 등을 활용해 구조적으로 작성해요.

## 2. 지식 문서 작성 형식

모든 지식 문서는 상단의 YAML 프론트매터와 하단의 마크다운 본문으로 구성돼요.

### YAML 프론트매터

문서 최상단에 `---`로 감싸서 메타데이터를 작성해요.

```yaml
---
type: Reference                    # 필수: 문서 유형 (예: Reference, Rule, Concept, Guide)
title: Open Knowledge Format (OKF) # 권장: 문서 제목
description: 규약에 대한 한 줄 요약이에요. # 권장: 검색 및 인덱스용 한 줄 요약
tags: [knowledge, standard]        # 선택: 분류를 위한 태그 목록
---
```

- `type` (필수): 지식의 종류를 나타내요.
  - `Reference`: 참조 자료 및 기술 규격
  - `Rule`: 반드시 지켜야 할 규칙이나 정책
  - `Concept`: 특정 도메인 용어나 개념 설명
  - `Guide`: 작업 수행 방법이나 안내
- `title` (권장): 문서의 공식 명칭을 적어요.
- `description` (권장): 한 문장으로 문서의 핵심 내용을 요약해요.
- `tags` (선택): 검색과 분류에 활용할 키워드 목록이에요.

### 마크다운 본문

프론트매터 아래에는 일반 마크다운으로 내용을 기술해요.

- 첫 번째 줄에는 문서의 제목(`# 제목`)을 작성해요.
- 핵심 내용을 바로 파악할 수 있도록 불필요한 서론을 줄이고 본론부터 설명해요.
- 표나 코드 블록, 목록을 적절히 활용해요.

## 3. 지식 인덱스 (index.md)

지식 디렉터리(`reference/knowledge/`)에는 탐색을 돕기 위한 특별한 파일인 `index.md`를 둬요.

- **프론트매터 생략**: `index.md`는 일반 지식 문서가 아니므로 YAML 프론트매터를 작성하지 않아요.
- **점진적 탐색 제공**: AI 에이전트나 사람이 모든 지식 문서를 한 번에 읽지 않고, `index.md` 목록을 먼저 훑어본 뒤 필요한 지식만 찾아 읽을 수 있게 해요.
- **목록 구성**: 상대 경로 링크와 한 줄 설명을 번호 또는 글머리 기호 목록으로 나열해요.

```markdown
# 지식 인덱스

- [Open Knowledge Format (OKF)](./open-knowledge-format.md): 사람과 AI 에이전트가 함께 읽고 쓰는 경량 지식 문서 규약이에요.
- [글쓰기 규칙](./writing-style.md): 작업 매뉴얼을 작성할 때 준수해야 하는 문체와 작성 지침이에요.
```
