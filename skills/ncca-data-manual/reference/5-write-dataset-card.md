# README 작성·개선

저장소의 `README.md`를 작성해 주세요.

README는 데이터를 분석·연구에 활용하려는 사람을 위한 Dataset Card 문서로 작성합니다.

## 방법

- `data/collection.json`과 실제 데이터를 바탕으로 저장소 루트의 `README.md`를 작성합니다.
- 데이터의 내용, 범위, 구조, 품질과 한계, 출처·라이선스, 다운로드·불러오기·해석 방법을 중심으로 설명합니다.
- 다음 공식 문서의 최신 내용을 따릅니다.
  - [Dataset Cards](https://huggingface.co/docs/hub/datasets-cards)
  - [Dataset Card metadata specification](https://github.com/huggingface/hub-docs/blob/main/datasetcard.md)
  - [Dataset Card template](https://github.com/huggingface/huggingface_hub/blob/main/src/huggingface_hub/templates/datasetcard_template.md)
  - [Manual Configuration](https://huggingface.co/docs/hub/datasets-manual-configuration)

# AI 추가 지침

- 데이터에 해당하는 메타데이터와 본문만 작성
- `collection.json`, 실제 데이터, README 간 내용 일치
- 출처·라이선스·제공자 등 근거 없는 정보의 추측 금지 및 사용자에게 근거 요청
- 저장소 구조, 데이터 생성 코드, 개발 환경, 배포 절차보다 소비자의 데이터 이해와 활용에 필요한 정보 우선
