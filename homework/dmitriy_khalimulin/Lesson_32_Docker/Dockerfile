FROM python
COPY program_for_docker.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["python", "program_for_docker.py"]