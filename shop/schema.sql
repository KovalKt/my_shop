drop table if exists product;
create table product (
  id integer primary key autoincrement,
  name text not null,
  price integer not null,
  picture_name text not null,
  amount_on_stock integer default 0
);
