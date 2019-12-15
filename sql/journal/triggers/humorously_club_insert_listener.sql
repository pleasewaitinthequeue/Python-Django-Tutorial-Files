create or replace trigger humorously_club_insert_listener
    after insert on humorously_club
    for each row
    
    begin
        insert into journal (
            entity_id,
            entity_name,
            entity_desc,
            created,
            entity_type
        )         
        values (
                --"ID" number(11,0)
            :new.id, --"ENTITY_ID" number(11,0),
            :new.name, --"ENTITY_NAME" nvarchar2(200),
            :new.title, --"ENTITY_DESC" nvarchar2(200),
            :new.created, --"CREATED" timestamp (6) not null enable,
            'Club' --primary key ("ID")
        );
    end;