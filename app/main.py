from typing import Optional

import uvicorn
from fastapi import FastAPI

from app.common.config import conf


def create_app():
    """
    �� �Լ� ����
    :return:
    """
    c = conf()
    app = FastAPI()

    # ������ ���̽� �̴ϼȶ�����

    # ���� �̴ϼȶ�����

    # �̵���� ����

    # ����� ����

    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)