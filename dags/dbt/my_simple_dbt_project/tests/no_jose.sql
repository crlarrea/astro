select * from {{ ref('model3') }}
where name is null or name = 'jose'