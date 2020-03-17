FROM python:3-slim
ADD detect-and-delete.py /
RUN pip install kubernetes
ENTRYPOINT "/"
CMD [ "python", "./detect-and-delete.py" ]