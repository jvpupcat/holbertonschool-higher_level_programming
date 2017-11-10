#!/usr/bin/python3
"""script that adds the State object "Louisiana" to hbtn_0e_6_usa"""

if __name__ == "__main__":
    import sqlalchemy
    from sqlalchemy.orm import sessionmaker
    import sqlalchemy.orm
    from model_state import Base, State
    import sys

    sub_lochost = 'mysql+mysqldb://{}:{}@localhost: 3306/{}'
    engine = sqlalchemy.create_engine(sub_lochost.format
                                      (sys.argv[1], sys.argv[2],
                                       sys.argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    update = session.query(State).filter(State.id == '2').first()
    update.name = 'New Mexico'
    session.commit()
    session.close()
