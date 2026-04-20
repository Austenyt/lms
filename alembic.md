### 3) База и модели
Создать структуру:
```
app/
  db/
    database.py
    base.py
  models/
    course.py
```

`app/db/database.py`
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./lms.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
```

`app/db/base.py`
```python
from sqlalchemy.orm import declarative_base

Base = declarative_base()
```

`app/models/course.py`
```python
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base

class Course(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    qty: Mapped[int] = mapped_column(Integer, nullable=False)
```

### 4) Alembic init и настройка
```bash
alembic init alembic
```

В `alembic.ini`:
```
sqlalchemy.url = sqlite:///./lms.db
```

В `alembic/env.py`:
```python
from app.db.base import Base
from app.models.course import Course

# ...

target_metadata = Base.metadata