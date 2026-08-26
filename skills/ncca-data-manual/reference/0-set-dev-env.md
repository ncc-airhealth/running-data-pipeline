# 0. 개발 환경 설정

데이터 파이프라인 개발 작업을 위해 필요한 환경을 설정해주세요.

## 완료 조건

다음의 조건들을 모두 만족하는 경우, [데이터 획득과 처리](reference/3-etl.md)으로 넘어갑니다.

- [ ] uv 설치 완료 - `uv --version`
- [ ] git 설치 완료 - `git --version`
- [ ] github-cli 설치 완료 - `gh --version`
- [ ] github-cli 인증 완료 - `gh auth status`
- [ ] huggingface-cli 설치 완료 - `hf --version`
- [ ] huggingface-cli 인증 완료 - `hf auth whoami`
- [ ] git lfs 설치 완료 - `git lfs --version`
- [ ] git xet 설치 완료 - `git xet --version`

## 작업 순서

다음 순서에 따라 현재 상태를 확인하고 **누락된 항목**만 설정해주세요.

1. [UV 공식 문서](https://docs.astral.sh/uv/getting-started/installation/)에 따라 `uv` 설치
2. [Git 설치 페이지](https://git-scm.com/downloads)를 통해 `git` 설치
3. [GitHub Cli 매뉴얼](https://cli.github.com/manual/)에 따라 `github cli` 설치 및 인증
4. [Git LFS 설치 섹션](https://git-lfs.com/)에 따라 `git lfs` 설치
5. [Git Xet 설치 섹션](https://huggingface.co/docs/hub/main/en/xet/using-xet-storage#git)에 따라 `git xet` 설치
6. 운영체제와 셸에 맞게 다음의 환경변수를 영구 설정해주세요. (NCCA_HF_NAMESPACE=husgbb)
7. (선택) Agent Skills를 설치해주세요. `npx skills install ncc-airhealth/running-data-pipeline`

# AI 추가 지침

- 기존 Git 설정, 로그인 계정, 셸 설정을 변경하려면 먼저 사람의 확인을 받는다.
- 로그인과 인증 정보 입력이 필요하면 사람에게 직접 진행하도록 요청한다.
- 설치 방법은 운영체제와 셸에 맞게 선택한다.
- 본문에 제시된 명령어로 결과를 검증한다.
- 작업을 마치면 설치한 도구의 버전, 로그인 계정, 환경변수, 설치한 스킬, 남은 작업을 정리해 보고한다.
