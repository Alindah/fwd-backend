# Building the image: docker build -t alindah/fwd_be:1.0 . 
# Starting the container: docker run -p 5000:5000 alindah/fwd_be:1.0

FROM python:3.9-alpine
COPY . /fwd
WORKDIR /fwd
RUN pip install -r requirements.txt
ENV PORT=5000
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["fwd_be.py"]