with featured_article as (
    select * from {{ref('int_content__featured_article')}}
)
select * from featured_article