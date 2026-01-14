with featured_book as (
    select *
    from {{ref("stg_content__books")}}
    order by random()
    fetch first 1 row only
)
select * from featured_book