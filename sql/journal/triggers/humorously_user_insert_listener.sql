create or replace trigger humorously_jokester_insert_listener
    after insert on auth_user
    for each row

    begin
        insert into journal (
            ENTITY_ID,
            ENTITY_NAME,
            ENTITY_DESC,
            CREATED,
            ENTITY_TYPE
        )         
        values (
                --"ID" number(11,0)
            :new.id, --"ENTITY_ID" number(11,0),
            :new.username, --"ENTITY_NAME" nvarchar2(200),
            :new.last_name || ', ' || :new.first_name, --"ENTITY_DESC" nvarchar2(200),
            :new.date_joined, --"CREATED" timestamp,
            'User' --"ENTITY_TYPE" nvarchar2(50),
        );
    end; 