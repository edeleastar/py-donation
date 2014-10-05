drop table if exists donations;
create table donations (
  id integer primary key autoincrement,
  amount integer not null,
  method text not null
);
