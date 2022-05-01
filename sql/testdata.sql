insert into branch (branch_name, city) values ('branch1', 'bei jing');

insert into branch (branch_name, city) values ('branch2', 'shang hai');

insert into department (department_id, department_name, department_type) values ('D00001', 'test_d_name', 'test_d_type');

insert into employee (employee_id, department_id, name, phone, address, is_manager, start_work_date) values ('E001', 'D00001', 'Reina', 'AGELOWV5YK361HJH', 'GC1RXHX 2LDH WD90S16682ICOCG9P6LS 822B36CS9544R4 FOSEXFNC8ML7REV', 1, '571-5-18');

insert into employee (employee_id, department_id, name, phone, address, is_manager, start_work_date) values ('E002', 'D00001', 'Kagura', 'N W4I0O8U19J8G82', 'GHJPCY2G T2FGXOXFGR CJPL6YJ2C0D97G IAJKYG5DAXFDAM6NDR MLX9Q3VTSL', 0, '777-2-5');

insert into employee (employee_id, department_id, name, phone, address, is_manager, start_work_date) values ('E003', 'D00001', 'Vivi', 'YMQH4L6QPGR6FA0G', '0UQ3XYQS02J1BFX7S7BRAMC64O7AH6YE6U979I0U5D9UDWK4R6U0QF6K8 UG8BKY', 0, '236-8-23');

insert into client (client_id, name, phone, address, contact_name, contact_phone, contact_email, relation) values ('C001', '4I5BQOVKY 0WYTE4', 'Y4 X PM82UHYG KH', 'MO0BJ0 1FDKKF 1KU8X5AUJ7RHDBVOEE6EKG2SNF8QKTWQ55RH6J70FPLH9N1JLG', '6S77OI6MC7H3STN3', 'EF2KP3L6PAKYOPQW', 'AGMX3523RPGVTGA60 ABMD9WK40BANIH', '2HPQOW4R6ROSOMMT');

insert into client (client_id, name, phone, address, contact_name, contact_phone, contact_email, relation) values ('C002', '6TH9AYX0BL LVIVL', 'Q4IHI 6VX OHE465', 'EKEAFHFV7ECY3YOTCR06G77OIP6OMFOTQ7LJMAX RB4JO0U4CA0LK32UNV9AAN0N', 'Q34P16O3T7CYLYUF', 'KWVR81QURFS7KDE6', 'V9K7FGERMKQXOLT8IE8BXBXTP  BC7UV', 'C34DJ17GUC41XMKT');

insert into client (client_id, name, phone, address, contact_name, contact_phone, contact_email, relation) values ('C003', '3BEXWS5KF2CVRDEW', '7I2TJVVIVW3FAHO ', '3Q5LPDYLVYXRA57PVPI12BG1R3E0QEA5Y SKQRMJ 3JGNHJFQ1LEKB582WB NSFR', ' R1P18UIXB4SYDHS', 'E6DVKGWCNGMRE3XC', '0CT9KH6DT94WIQ7HRNL4B2AEUG7CB 42', 'LGPEW9BXHJCLK6 E');

insert into client (client_id, name, phone, address, contact_name, contact_phone, contact_email, relation) values ('C004', 'U418J90679LAEVB6', '02FJDMMVN0CW392I', 'NT0JQRUK8URRBVV29317MB R1U QKNKXXXPBC7QMV0GNKW2FIFVDS5K2SVDRX3GK', '7O6AMUPB5T1QPWS4', 'LS61I9 OB387Q5W2', 'JH3ABTKE NURTW57BSOLH82MAAUONT B', 'QNI4FE273PCRQV H');

insert into client (client_id, name, phone, address, contact_name, contact_phone, contact_email, relation) values ('C005', '6BID LL P2AY4C6K', 'CQQ8NMLTEMPYUEVH', 'KGSC3ODVCHSVC5JC2XV IC3O7D4LEHIOVR9RUR8AXOVB3AEPH6H27WMNCE6HJIYQ', 'B805TEA 4YK4I3 A', 'I8HQBPQDL0A8XBPT', 'P86B1O85D6R9LF MPILHAHJX0NLFA UG', 'HYKPWYGDDEK7WL9 ');

insert into saving_account (account_id, branch_name, balance, open_date, rate, currency_type) values ('C BG5H', 'branch1', 0, '1772-12-8', 4, 1);

insert into saving_account (account_id, branch_name, balance, open_date, rate, currency_type) values ('WBO8DX', 'branch2', 2, '820-4-8', 0, 4);

insert into saving_account (account_id, branch_name, balance, open_date, rate, currency_type) values ('SMQI2B', 'branch1', 4, '467-10-22', 1, 3);

insert into client_saving_account (client_id, account_id, latest_visit_date) values ('C001', 'C BG5H', '1002-4-11 9:34:46');

insert into client_saving_account (client_id, account_id, latest_visit_date) values ('C002', 'WBO8DX', '440-11-11 4:41:32');

insert into client_saving_account (client_id, account_id, latest_visit_date) values ('C003', 'SMQI2B', '1-1-1 0:0:0');

insert into checking_account (account_id, branch_name, balance, open_date, overdraft) values ('8J 18 ', 'branch1', 2, '398-3-17', 1);

insert into client_check_account (client_id, account_id, latest_visit_date) values ('C001', '8J 18 ', '930-3-8 13:33:36');

insert into loan (loan_id, branch_name, loan_money) values ('LN0001', 'branch2', 1);

insert into pay_loan (loan_id, pay_date, pay_money) values ('LN0001', '1129-9-10', 1);

insert into client_loan (client_id, loan_id) values ('C001', 'LN0001');