
### Создать структуру:
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
### Alembic init и настройка
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

