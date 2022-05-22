/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2022/4/29 19:26:10                           */
/*==============================================================*/


SET FOREIGN_KEY_CHECKS = 0;

drop table if exists branch;

drop table if exists checking_account;

drop table if exists client;

drop table if exists client_check_account;

drop table if exists client_loan;

drop table if exists client_saving_account;

drop table if exists department;

drop table if exists employee;

drop table if exists loan;

drop table if exists pay_loan;

drop table if exists responsible;

drop table if exists saving_account;

SET FOREIGN_KEY_CHECKS = 1;

/*==============================================================*/
/* Table: branch                                                */
/*==============================================================*/
create table branch
(
   branch_name          varchar(16) not null,
   city                 varchar(16) not null,
   primary key (branch_name)
);

/*==============================================================*/
/* Table: checking_account                                      */
/*==============================================================*/
create table checking_account
(
   account_id           char(6) not null,
   branch_name          varchar(16) not null,
   balance              float(8,2) not null,
   open_date            date not null,
   overdraft            float(8,2) not null,
   primary key (account_id)
);

/*==============================================================*/
/* Table: client                                                */
/*==============================================================*/
create table client
(
   client_id            char(4) not null,
   name                 varchar(16) not null,
   phone                varchar(16) not null,
   address              varchar(64) not null,
   contact_name         varchar(16) not null,
   contact_phone        varchar(16) not null,
   contact_email        varchar(32) not null,
   relation             varchar(16) not null,
   primary key (client_id)
);

/*==============================================================*/
/* Table: client_check_account                                  */
/*==============================================================*/
create table client_check_account
(
   client_id            char(4) not null,
   account_id           char(6) not null,
   latest_visit_date    date,
   primary key (client_id, account_id)
);

/*==============================================================*/
/* Table: client_loan                                           */
/*==============================================================*/
create table client_loan
(
   client_id            char(4) not null,
   loan_id              char(6) not null,
   primary key (client_id, loan_id)
);

/*==============================================================*/
/* Table: client_saving_account                                 */
/*==============================================================*/
create table client_saving_account
(
   client_id            char(4) not null,
   account_id           char(6) not null,
   latest_visit_date    date,
   primary key (client_id, account_id)
);

/*==============================================================*/
/* Table: department                                            */
/*==============================================================*/
create table department
(
   department_id        char(6) not null,
   department_name      varchar(16) not null,
   department_type      varchar(16) not null,
   primary key (department_id)
);

/*==============================================================*/
/* Table: employee                                              */
/*==============================================================*/
create table employee
(
   employee_id          char(4) not null,
   department_id        char(6),
   name                 varchar(16) not null,
   phone                varchar(16) not null,
   address              varchar(64) not null,
   is_manager           bool not null,
   start_work_date      date not null,
   primary key (employee_id)
);

/*==============================================================*/
/* Table: loan                                                  */
/*==============================================================*/
create table loan
(
   loan_id              char(6) not null,
   branch_name          varchar(16) not null,
   loan_money           float(8,2) not null,
   primary key (loan_id)
);

/*==============================================================*/
/* Table: pay_loan                                              */
/*==============================================================*/
create table pay_loan
(
   loan_id              char(6) not null,
   pay_date             date not null,
   pay_money            float(8,2) not null,
   primary key (loan_id, pay_date)
);

/*==============================================================*/
/* Table: responsible                                           */
/*==============================================================*/
create table responsible
(
   client_id            char(4) not null,
   employee_id          char(4) not null,
   responsible_type     bool not null,
   primary key (client_id, employee_id)
);

/*==============================================================*/
/* Table: saving_account                                        */
/*==============================================================*/
create table saving_account
(
   account_id           char(6) not null,
   branch_name          varchar(16) not null,
   balance              float(8,2) not null,
   open_date            date not null,
   rate                 float not null,
   currency_type        varchar(16) not null,
   primary key (account_id)
);

alter table checking_account add constraint FK_check_branch foreign key (branch_name)
      references branch (branch_name) on delete restrict on update restrict;

alter table client_check_account add constraint FK_client_check_account foreign key (client_id)
      references client (client_id) on delete restrict on update restrict;

alter table client_check_account add constraint FK_client_check_account2 foreign key (account_id)
      references checking_account (account_id) on delete cascade on update restrict;

alter table client_loan add constraint FK_client_loan foreign key (client_id)
      references client (client_id) on delete restrict on update restrict;

alter table client_loan add constraint FK_client_loan2 foreign key (loan_id)
      references loan (loan_id) on delete restrict on update restrict;

alter table client_saving_account add constraint FK_client_saving_account foreign key (client_id)
      references client (client_id) on delete restrict on update restrict;

alter table client_saving_account add constraint FK_client_saving_account2 foreign key (account_id)
      references saving_account (account_id) on delete cascade on update restrict;

alter table employee add constraint FK_employee_work_department foreign key (department_id)
      references department (department_id) on delete restrict on update restrict;

alter table loan add constraint FK_branch_loan foreign key (branch_name)
      references branch (branch_name) on delete restrict on update restrict;

alter table pay_loan add constraint FK_loan_payment foreign key (loan_id)
      references loan (loan_id) on delete restrict on update restrict;

alter table responsible add constraint FK_responsible foreign key (client_id)
      references client (client_id) on delete restrict on update restrict;

alter table responsible add constraint FK_responsible2 foreign key (employee_id)
      references employee (employee_id) on delete restrict on update restrict;

alter table saving_account add constraint FK_saving_branch foreign key (branch_name)
      references branch (branch_name) on delete restrict on update restrict;

