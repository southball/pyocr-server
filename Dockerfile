FROM ubuntu:22.04
RUN apt update && apt install -y python3 python3-pip tesseract-ocr tesseract-ocr-jpn
RUN pip install flask pyocr
COPY server.py /app/server.py
EXPOSE 5000
WORKDIR /app
ENTRYPOINT ["flask", "--app", "server", "run"]
CMD ["--host=0.0.0.0"]
