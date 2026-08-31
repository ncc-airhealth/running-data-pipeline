# 5. Dataset Card 작성·개선

저장소 루트의 `README.md`를 Hugging Face Dataset Card로 작성해요.
데이터를 분석·연구에 활용하려는 사람이 적합성을 판단하고 올바르게 해석할 수 있도록 설명하세요.

## 완료 조건

다음 조건을 모두 만족하면 Dataset Card 작성이 끝나요.

- [ ] README 상단의 YAML 메타데이터가 Hugging Face 형식에 맞음
- [ ] `data/collection.json`, 실제 데이터, README의 내용이 서로 일치함
- [ ] README만 읽고 데이터의 내용, 범위, 구조, 품질, 한계, 출처, 라이선스를 확인할 수 있음
- [ ] 비어 있거나 현재 데이터에 해당하지 않는 항목이 없음

## 방법

- README 상단에 Hugging Face가 인식하는 YAML 메타데이터를 작성하세요.
- `data/collection.json`과 실제 데이터를 근거로 Markdown 본문을 작성하세요.
- 데이터의 목적, 시간·공간 범위, 관측 단위, 파일 구조, 변수와 단위, 품질과 한계, 출처와 라이선스를 데이터 특성에 맞게 설명하세요.
- 수집·처리 과정이 데이터의 의미나 품질에 영향을 주었다면 그 내용과 영향을 설명하세요.
- 낯선 전문 용어는 처음 나올 때 한 문장으로 설명하세요.
- 원본 라이선스의 고지 의무나 사용자 요구가 있을 때만 별도 `LICENSE` 또는 `NOTICE` 파일을 추가하세요.
- 다음 공식 문서의 최신 내용을 따르세요.
  - [Dataset Cards](https://huggingface.co/docs/hub/datasets-cards)
  - [Dataset Card metadata specification](https://github.com/huggingface/hub-docs/blob/main/datasetcard.md)
  - [Dataset Card template](https://github.com/huggingface/huggingface_hub/blob/main/src/huggingface_hub/templates/datasetcard_template.md)
  - [Manual Configuration](https://huggingface.co/docs/hub/datasets-manual-configuration)
- 공식 템플릿은 누락된 내용을 확인하는 기준으로 사용하세요.
- 현재 데이터를 이해하고 활용하는 데 필요한 항목만 선택하세요.

# AI 추가 지침

- 현재 데이터에 해당하는 YAML 메타데이터와 본문만 작성하세요.
- 출처, 라이선스, 제공자 등 근거가 없는 정보는 추측하지 말고 사용자에게 근거를 요청하세요.
- 데이터 수집·처리는 데이터의 의미, 품질, 한계에 영향을 주는 내용만 개념적으로 설명하세요.
- 사용자가 요청하지 않았다면 일반적인 다운로드·불러오기 코드, 저장소 복제, 로컬 파일 읽기 방법을 제외하세요.
- 개발 환경, 패키지 설치, 환경 변수, 스크립트 실행, 의존성 잠금, 데이터 재현·검증·배포 절차와 Git 작업을 제외하세요.
- 특수한 접근 조건이나 데이터별 config·split 선택이 필요할 때만 최소한으로 안내하세요.
- 변수 조합, 결합 키, 조회 방법을 모르면 데이터를 잘못 해석하는 경우에만 이를 설명하세요.
- 해당하지 않는 제목, 빈 항목, 일반적인 Hugging Face 사용법을 제외하세요.
- Markdown 본문에서는 문장이 끝날 때마다 줄을 바꾸세요.
- 데이터 파일이나 변수를 표로 정리할 때는 한 행에 하나씩 쓰고 용도를 함께 설명하세요.
