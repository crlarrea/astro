with featured_post as (
    select * from {{ref('int_content__featured_post')}}
)
select * from featured_post