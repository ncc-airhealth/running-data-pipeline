# README 작성·개선

저장소의 `README.md`를 작성해 주세요.

README는 데이터를 분석·연구에 활용하려는 사람이 데이터가 목적에 맞는지 판단하고 올바르게 해석할 수 있도록 작성합니다.

## 완료 조건

다음 조건을 모두 만족하면 이 단계를 완료하고 `SKILL.md`의 다음 미완료 단계로 넘어갑니다.

- [ ] Hugging Face의 최신 Dataset Card 형식과 메타데이터 규칙을 따른다.
- [ ] `data/collection.json`, 실제 데이터, README의 내용이 서로 일치한다.
- [ ] README만 읽고 데이터의 내용, 범위, 구조, 품질, 출처를 확인할 수 있다.
- [ ] 각 항목에는 이 데이터를 이해하고 활용하는 데 필요한 내용이 담겨 있다.

## 방법

- `data/collection.json`과 실제 데이터를 바탕으로 저장소 루트의 `README.md`를 작성합니다.
- 데이터의 특성에 맞춰 내용과 목적, 시간·공간 범위, 관측 단위, 구조, 변수와 단위, 품질과 한계, 출처와 라이선스를 설명합니다.
- 수집·처리 과정이 데이터의 의미나 품질에 영향을 준 경우, 그 내용과 영향을 설명합니다.
- 낯선 전문용어는 처음 나올 때 한 문장으로 쉽게 설명합니다.
- 별도 `LICENSE`·`NOTICE` 파일은 원본 라이선스 조건, 고지 의무 또는 사용자 요구가 있을 때 추가합니다.
- 다음 공식 문서의 최신 내용을 따릅니다.
  - [Dataset Cards](https://huggingface.co/docs/hub/datasets-cards)
  - [Dataset Card metadata specification](https://github.com/huggingface/hub-docs/blob/main/datasetcard.md)
  - [Dataset Card template](https://github.com/huggingface/huggingface_hub/blob/main/src/huggingface_hub/templates/datasetcard_template.md)
  - [Manual Configuration](https://huggingface.co/docs/hub/datasets-manual-configuration)
- 공식 문서의 형식, 메타데이터 규칙, Dataset Card 작성 원칙을 전반적으로 반영합니다.
- 공식 템플릿은 작성 항목을 검토하는 기준으로 사용하고, 이 데이터를 이해하고 활용하는 데 필요한 항목을 선택하여 작성합니다.

# AI 추가 지침

- 현재 데이터에 해당하는 YAML 메타데이터와 본문만 작성
- `collection.json`, 실제 데이터, README 간 내용 일치
- 출처·라이선스·제공자 등 근거 없는 정보의 추측 금지 및 사용자에게 근거 요청
- 데이터 수집·처리는 데이터의 의미·품질·한계에 영향을 주는 내용만 개념적으로 설명
- 사용자의 명시적 요청이 없는 일반적인 다운로드·불러오기 안내와 코드 예제, 저장소 복제, 로컬 파일 읽기 방법 제외
- 개발 환경, 패키지 설치, 환경 변수, 처리 스크립트 실행, 의존성 잠금, 데이터 재현·검증·배포를 위한 실행 절차와 Git 작업 제외
- 특수한 접근 조건이나 데이터별 config·split 선택이 필요한 경우에만 최소한으로 안내
- 변수 조합, 결합 키, 조회 방법은 이를 모르면 데이터를 잘못 해석하는 경우에만 설명
- 해당하지 않는 제목, 빈 항목, 일반적인 Hugging Face 사용법 제외
- Markdown 본문에서 문장이 끝날 때마다 줄바꿈
- 데이터 파일이나 변수를 표로 정리할 때는 한 행에 하나씩 쓰고 용도를 함께 설명
