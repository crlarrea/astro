with featured_post as (
    select
        created_at,
        post
    from {{ref("stg_content__posts")}}
    order by
        created_at DESC
    fetch first 1 row only
)
select * from featured_post