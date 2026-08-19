---
name: ncca-data-manual
description: ncca Hugging Face dataset repo 관리 메뉴얼
---

# ncca Hugging Face dataset repo 관리 메뉴얼

## 규칙

- Dataset Repository는 기본적으로 private으로 설정
- git stage/commit/push는 인간만 가능 (에이전트는 금지)
- 데이터, Dataset Card, STAC의 내용과 경로를 일치시킴

## 데이터셋 레포 경로 구성 Best Practice

```
<organization>/<dataset-id>/
├── assets/
│   └── <asset-name>.<extension>
├── items/
│   └── <item-id>/
│       ├── <item-id>.json
│       └── <asset-name>.<extension>
├── collection.json
├── process.py
├── process.py.lock
└── README.md
```

## 데이터셋 레포 작업 순서

1. 대상 데이터 정의
2. `데이터에 대한 정보` 조사 및 수집
3. 데이터 수집/처리/검토 - [write-process-script.md](reference/write-process-script.md) 참고
4. STAC metadata JSON 작성/개선 - [write-stac-static-catalog.md](reference/write-stac-static-catalog.md) 참고
5. Dataset Card 작성/개선 - [write-readme.md](reference/write-readme.md) 참고
6. 검토 및 피드백 (반드시 인간이 수행)
7. 완료
