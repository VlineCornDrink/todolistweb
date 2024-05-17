FROM python:3

# Python 출력이 버퍼링되지 않도록 설정
ENV PYTHONUNBUFFERED 1

# 애플리케이션 코드를 위한 디렉토리를 생성
RUN mkdir /app

# 작업 디렉토리를 설정
WORKDIR /app

# requirements.txt 파일을 컨테이너로 복사
COPY requirements.txt /app/

# pip를 업그레이드하고 requirements.txt 파일에 명시된 패키지를 설치
RUN pip install --upgrade pip && pip install -r requirements.txt

# 현재 디렉토리의 모든 파일을 컨테이너로 복사
COPY . /app/

# 호스트 시스템의 8000번 포트를 외부에 노출
EXPOSE 8000

