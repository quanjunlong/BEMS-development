# Dockerfile과 같은 디렉터리에 .dockerignore 파일을 다음 내용으로 만드세요.
# 이는 Docker 이미지에 로컬 모듈과 디버깅 로그를 복사하는 것을 막아서 이미지 내에서 설치한 모듈을 덮어쓰지 않게 합니다

node_modules
npm-debug.log
