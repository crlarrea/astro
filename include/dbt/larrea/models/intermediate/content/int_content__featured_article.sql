with featured_article as (
    select
        article_title,
        slug,
        article_short_description,
        article_image,
        updated_at
    from {{ref("stg_content__articles")}}
    order by
        random()
    fetch first 1 row only
)
select * from featured_article