#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa"""

if __name__ == "__main__":
    import sqlalchemy
    from sqlalchemy.orm import sessionmaker
    import model_state
    import sys

    engine = sqlalchemy.create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'\
                                      .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    model_state.Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(model_state.State).order_by(model_state.State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
