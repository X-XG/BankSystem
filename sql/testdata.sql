insert into branch (branch_name, city) values ('branch1', 'bei jing');

insert into branch (branch_name, city) values ('branch2', 'shang hai');

insert into department (department_id, department_name, department_type) values ('D001', 'test_d_name', 'test_d_type');

insert into employee (employee_id, department_id, name, phone, address, is_manager, start_work_date) values ('E001', 'D001', 'Reina', 'AGELOWV5YK361HJH', 'GC1RXHX 2LDH WD90S16682ICOCG9P6LS 822B36CS9544R4 FOSEXFNC8ML7REV', 1, '571-5-18');

insert into employee (employee_id, department_id, name, phone, address, is_manager, start_work_date) values ('E002', 'D001', 'Kagura', 'N W4I0O8U19J8G82', 'GHJPCY2G T2FGXOXFGR CJPL6YJ2C0D97G IAJKYG5DAXFDAM6NDR MLX9Q3VTSL', 0, '777-2-5');

insert into employee (employee_id, department_id, name, phone, address, is_manager, start_work_date) values ('E003', 'D001', 'Vivi', 'YMQH4L6QPGR6FA0G', '0UQ3XYQSA2J1BFX7S7BRAMC64O7AH6YE6U979I0U5D9UDWK4R6U0QF6K8 UG8BKY', 0, '236-8-23');

insert into client (client_id, name, phone, address, contact_name, contact_phone, contact_email, relation) values ('C001', 'Migasa', '114511', 'MO0BJ0 1FDKKF 1KU8X5AUJ7RHDBVOEE6EKG2SNF8QKTWQ55RH6J70FPLH9N1JLG', 'contactname', '10011', 'test1@gmail.com', 'npy');

insert into client (client_id, name, phone, address, contact_name, contact_phone, contact_email, relation) values ('C002', 'Tatakei', '911', 'EKEAFHFV7ECY3YOTCR06G77OIP6OMFOTQ7LJMAX RB4JO0U4CA0LK32UNV9AAN0N', 'contactname', '10011', 'test2@gmail.com', 'mpy');

insert into client (client_id, name, phone, address, contact_name, contact_phone, contact_email, relation) values ('C003', 'Yuyichi', '114512', '3Q5LPDYLVYXRA57PVPI12BG1R3E0QEA5Y SKQRMJ 3JGNHJFQ1LEKB582WB NSFR', 'contactname', '10011', 'test3@gmail.com', 'cpy');

insert into client (client_id, name, phone, address, contact_name, contact_phone, contact_email, relation) values ('C004', 'Vanila', '888888', 'NT0JQRUK8URRBVV29317MB R1U QKNKXXXPBC7QMV0GNKW2FIFVDS5K2SVDRX3GK', 'contactname', '10011', 'tes4t@gmail.com', 'kpy');

insert into client (client_id, name, phone, address, contact_name, contact_phone, contact_email, relation) values ('C005', 'Chocola', '23333', 'KGSC3ODVCHSVC5JC2XV IC3O7D4LEHIOVR9RUR8AXOVB3AEPH6H27WMNCE6HJIYQ', 'contactname', '10011', 'test5@gmail.com', 'tpy');

insert into saving_account (account_id, branch_name, balance, open_date, rate, currency_type) values ('SA01', 'branch1', 0, '1772-12-8', 4, 1);

insert into saving_account (account_id, branch_name, balance, open_date, rate, currency_type) values ('SA02', 'branch2', 2, '820-4-8', 0, 4);

insert into saving_account (account_id, branch_name, balance, open_date, rate, currency_type) values ('SA03', 'branch1', 4, '467-10-22', 1, 3);

insert into client_saving_account (client_id, account_id, latest_visit_date) values ('C001', 'SA01', '1002-4-11');

insert into client_saving_account (client_id, account_id, latest_visit_date) values ('C002', 'SA02', '440-11-11');

insert into client_saving_account (client_id, account_id, latest_visit_date) values ('C003', 'SA03', '1-1-1');

insert into checking_account (account_id, branch_name, balance, open_date, overdraft) values ('CA01', 'branch1', 2, '398-3-17', 1);

insert into client_check_account (client_id, account_id, latest_visit_date) values ('C001', 'CA01', '930-3-8 13:33:36');

insert into loan (loan_id, branch_name, loan_money, status) values ('LN01', 'branch2', 10, 'issuing');

insert into pay_loan (loan_id, pay_date, pay_money) values ('LN01', '1129-9-10', 1);

insert into client_loan (client_id, loan_id) values ('C001', 'LN01');