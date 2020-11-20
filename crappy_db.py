import os

# file format:
# <student id>,<first name>,<last name>

DB_FILENAME = "crappy_db.txt"
TMP_FILENAME = "updated_db.txt"


def create_record(id, first_name, last_name):
    return f"{id},{first_name},{last_name}\n"


def setup():
    # create a folder called 'data'
    if not os.path.isdir('data'):
        os.mkdir('data')
    os.chdir('data')


def insert_data():
    records = [
        ['w000001', 'john', 'smith'],
        ['w000002', 'jane', 'doe'],
        ['w000003', 'jack', 'sprat']
    ]
    f = open(DB_FILENAME, 'w')
    for r in records:
        id, first_name, last_name = r
        f.write(create_record(id, first_name, last_name))
    f.close()


def select_data():
    with open(DB_FILENAME) as f:
        for line in f:
            id, first_name, last_name = line.rstrip('\n').split(',')
            print(f"id:{id}, name: {first_name} {last_name}")


def delete_data(surname):
    infile = open(DB_FILENAME)
    outfile = open(TMP_FILENAME, "w")
    for line in infile:
        id, first_name, last_name = line.rstrip('\n').split(',')
        if last_name.lower() != surname.lower():
            outfile.write(create_record(id, first_name, last_name))
    outfile.close()
    infile.close()
    os.replace(TMP_FILENAME, DB_FILENAME)


def update_data():
    infile = open(DB_FILENAME)
    outfile = open(TMP_FILENAME, "w")
    for line in infile:
        id, first_name, last_name = line.rstrip('\n').split(',')
        if id.lower() == "w000003":
            record = create_record("w000002", first_name, last_name)
        else:
            record = create_record(id, first_name, last_name)
        outfile.write(record)
    outfile.close()
    infile.close()
    os.replace(TMP_FILENAME, DB_FILENAME)


def main():
    # all the stuff when run as a program goes here
    setup()
    insert_data()
    select_data()
    delete_data("Doe")
    update_data()


if __name__ == "__main__":
    # I am being run as a standalone program!
    main()
