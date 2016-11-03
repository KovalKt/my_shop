drop table if exists product;
create table product (
  id integer primary key autoincrement,
  name text not null,
  price integer not null
);
