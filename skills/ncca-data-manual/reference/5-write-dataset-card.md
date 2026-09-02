# 5. Dataset Card 작성·개선

Dataset Card는 Hugging Face 데이터셋 저장소 루트의 `README.md`에 작성하는 데이터 설명 문서예요.
데이터를 연구·분석에 활용하려는 사람이 데이터가 목적에 적합한지 판단하고 올바르게 해석할 수 있도록 작성하세요.

## 완료 조건

다음 조건을 모두 만족하면 Dataset Card 작성이 끝나요.

- [ ] `README.md` 상단의 YAML 메타데이터가 Hugging Face 형식을 따름
- [ ] `data/collection.json`, 실제 데이터, `README.md`의 내용이 서로 일치함
- [ ] [Dataset Card 템플릿](../assets/dataset-card-template.md)에 따라 현재 데이터에 필요한 내용을 작성함
- [ ] 템플릿의 `{{ ... }}`와 `<!-- ... -->`가 남아 있지 않음
- [ ] 비어 있거나 현재 데이터에 해당하지 않는 항목이 없음
- [ ] 본문이 [테크니컬 라이팅](technical-writing.md)의 기준에 맞음

## 작성 방법

- [테크니컬 라이팅](technical-writing.md)을 따라 Dataset Card를 작성하세요.
- [Dataset Card 템플릿](../assets/dataset-card-template.md)을 복사하여 저장소 루트의 `README.md`로 사용하세요.
  - 템플릿의 모든 `{{ ... }}`를 실제 내용으로 바꾸세요.
  - 템플릿의 `<!-- ... -->` 안내에 따라 내용을 작성한 뒤 주석을 삭제하세요.
  - 템플릿에서 현재 데이터를 이해하고 활용하는 데 필요한 항목만 작성하세요.
  - 템플릿에서 현재 데이터에 해당하지 않는 표의 행이나 섹션은 제목까지 삭제하세요.
- 낯선 전문 용어는 처음 나올 때 한 문장으로 설명하세요.
- 원본 라이선스의 고지 의무나 사용자 요구가 있을 때만 별도 `LICENSE` 또는 `NOTICE` 파일을 추가하세요.
- `data/collection.json`과 실제 데이터를 근거로 Markdown 본문을 작성하세요.
- Dataset Card의 역할과 메타데이터 사용 방법은 [Dataset Cards](https://huggingface.co/docs/hub/datasets-cards)를 확인하세요.
- YAML 메타데이터의 필드와 값은 [Dataset Card metadata specification](https://github.com/huggingface/hub-docs/blob/main/datasetcard.md)을 따르세요.
- 공식 식별자가 없는 라이선스는 `license: other`로 지정하고 `license_name`과 `license_link`를 함께 작성하세요.
- `license_name`은 `^[a-z0-9-.]+$` 형식의 Hugging Face Hub 식별자로 작성하세요. 한국어 공식 명칭은 Dataset Card 본문과 STAC 라이선스 링크의 `title`에 작성하세요.
- Dataset Viewer와 데이터 로더에서 파일 구성, `config`, `split`, 불러오기 옵션을 직접 설정해야 할 때는 [Manual Configuration](https://huggingface.co/docs/hub/datasets-manual-configuration)을 따르세요.
- 여러 입력을 조인하거나 값을 대체했다면 각 입력에서 가져온 값과 적용한 규칙을 설명하세요.

> [!NOTE]
> Dataset Viewer는 Hugging Face Hub에서 데이터 내용을 미리 보는 기능이에요.
> 데이터 로더는 데이터 파일을 `config`와 `split`에 따라 불러오는 기능이에요.


# AI 추가 지침

- 출처, 라이선스, 제공자 등 근거가 없는 정보는 추측하지 말고 사용자에게 근거를 요청하세요.
- 사용자가 요청하지 않았다면 일반적인 Hugging Face 사용법, 다운로드·불러오기 코드, 저장소 복제, 로컬 파일 읽기 방법을 제외하세요.
- 개발 환경, 패키지 설치, 환경 변수, 스크립트 실행, 의존성 잠금, 데이터 재현·검증·배포 절차와 Git 작업을 제외하세요.
- 특수한 접근 조건이나 데이터별 `config`·`split` 선택이 필요할 때만 최소한으로 안내하세요.
- 변수 조합, 결합 키, 조회 방법을 모르면 데이터를 잘못 해석하는 경우에만 이를 설명하세요.
- Markdown 본문에서는 문장이 끝날 때마다 줄을 바꾸세요.
- 같은 규칙으로 반복되는 데이터 파일은 경로 패턴으로 묶어 표의 한 행에 작성하세요. 정확한 파일 목록은 STAC Asset으로 제공하세요.
- 반복되지 않는 데이터 파일과 변수는 표의 한 행에 하나씩 작성하고 용도를 함께 설명하세요.
