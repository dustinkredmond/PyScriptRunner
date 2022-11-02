create table if not exists script(
    id integer not null primary key autoincrement,
    name text not null,
    code text not null
)