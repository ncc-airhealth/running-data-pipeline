---
name: ncca-set-dev-env
description: NCCA 데이터 파이프라인 작업에 필요한 CLI, Git 대용량 파일 확장, 계정 인증, 환경 변수를 설정하고 검증할 때 사용한다.
---

# NCCA 데이터 파이프라인 개발 환경 설정

새로운 컴퓨터에서 NCCA 데이터 파이프라인 작업을 시작하거나 필요한 도구와 설정이 누락된 경우 개발 환경을 설정해요. 먼저 현재 상태를 확인하고 누락된 항목만 설정하세요.

## 완료 조건

다음 조건을 모두 만족하면 개발 환경 설정이 끝나요.

- [ ] `uv` 설치 완료: `uv --version`
- [ ] Git 설치 완료: `git --version`
- [ ] GitHub CLI 설치 완료: `gh --version`
- [ ] GitHub CLI 인증 완료: `gh auth status`
- [ ] Hugging Face CLI 설치 완료: `hf --version`
- [ ] Hugging Face CLI 인증 완료: `hf auth whoami`
- [ ] Git Large File Storage(Git LFS) 설치 완료: `git lfs --version`
- [ ] Git Xet 설치 완료: `git xet --version`
- [ ] Git LFS와 Git Xet 연동 설정 완료: `git lfs install`, `git xet install`
- [ ] `NCCA_HF_NAMESPACE` 환경 변수의 값이 `husgbb`로 설정됨

## 설정 방법

1. 완료 조건에 있는 명령어로 현재 상태를 확인하세요.
2. 누락된 도구를 운영체제에 맞게 설치하세요.
   - [`uv` 설치 문서](https://docs.astral.sh/uv/getting-started/installation/)
   - [Git 설치 문서](https://git-scm.com/downloads)
   - [GitHub CLI 설치 문서](https://github.com/cli/cli#installation)
   - [Hugging Face CLI 문서](https://huggingface.co/docs/huggingface_hub/guides/cli)
   - [Git LFS 설치 문서](https://git-lfs.com/)
   - [Git Xet 설치 문서](https://huggingface.co/docs/hub/xet/using-xet-storage#git)
3. `gh auth login`과 `hf auth login`을 실행하여 사용할 계정으로 인증하세요.
4. `git lfs install`과 `git xet install`을 한 번씩 실행하여 Git에 연동하세요.
5. 운영체제와 셸에 맞게 `NCCA_HF_NAMESPACE=husgbb` 환경 변수를 영구 설정하세요. 새 셸을 열고 설정값을 확인하세요.
6. 완료 조건에 있는 명령어를 다시 실행하여 결과를 확인하세요.

필요하면 다음 명령어로 이 저장소의 Agent Skills를 설치하세요.

```bash
npx skills add ncc-airhealth/running-data-pipeline
```

# AI 추가 지침

- 완료 조건을 먼저 확인하고 누락된 항목만 설정하세요.
- 설치 방법은 사용자의 운영체제와 셸에 맞게 공식 문서에서 선택하세요.
- 기존 Git 설정, 로그인 계정, 셸 설정을 변경하기 전에 사용자에게 확인하세요.
- 로그인이나 인증 정보 입력이 필요하면 사용자가 직접 진행하도록 요청하세요.
- 작업을 마치면 설치한 도구의 버전, 인증된 계정, 환경 변수, 설치한 스킬, 남은 작업을 보고하세요.
