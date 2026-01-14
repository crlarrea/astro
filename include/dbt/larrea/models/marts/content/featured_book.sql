with featured_book as (
    select * from {{ref('int_content__featured_book')}}
)
select * from featured_book