import os

# file format:
# <student id>,<first name>,<last name>

DB_FILENAME = "crappy_db.txt"
TMP_FILENAME = "updated_db.txt"


def create_record(id, first_name, last_name):
    return f"{id},{first_name},{last_name}\n"


def get_fields(line):
    id, first_name, last_name = line.rstrip('\n').lower().split(',')
    return {"id":id, "first_name":first_name, "last_name":last_name}


def read_file():
    infile = open(DB_FILENAME)
    for line in infile:
        d = get_fields(line)
        yield d
    infile.close()


def create_temp_file():
    outfile = open(TMP_FILENAME, "w")
    outfile.close()


def update_file(fields):
    outfile = open(TMP_FILENAME, "a")
    outfile.write(create_record(**fields))
    outfile.close()


def replace_file():
    os.replace(TMP_FILENAME, DB_FILENAME)


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
    for d in read_file():
        print(f"id:{d['id']}, name: {d['first_name']} {d['last_name']}")


def delete_data(last_name):
    create_temp_file()
    for d in read_file():
        if d['last_name'] != last_name.lower():
            update_file(d)
    replace_file()


def update_data():
    create_temp_file()
    for d in read_file():
        if d['id'] == "w000003":
            d['id'] = "w000002"
        update_file(d)
    replace_file()


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
