#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa"""

if __name__ == "__main__":
    import sqlalchemy
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    import sys

    sub_lochost = 'mysql+mysqldb://{}:{}@localhost: 3306/{}'
    engine = sqlalchemy.create_engine(sub_lochost.format
                                      (sys.argv[1], sys.argv[2],
                                       sys.argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    a_state = session.query(State).filter(State.name.op('REGEXP')
                                          ('a')).order_by(State.id)
    for state in a_state:
        print("{0.id}: {0.name}".format(state))
    session.close()
