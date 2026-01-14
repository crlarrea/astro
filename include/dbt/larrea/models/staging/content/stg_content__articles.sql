with

source as (

    select * from {{ source('content', 'articles') }}

),

renamed as (

    select

        ----------  ids
        id as article_id,

        ---------- strings
        title as article_title,
        TRIM(REGEXP_REPLACE(REGEXP_REPLACE(REPLACE(LOWER(title),' ', '-'),'[^a-z0-9-]', '', 'g'),'-+', '-', 'g')) as slug,
        short_description as article_short_description,
        body as article_body,
        image as article_image,
        taxonomy as taxonomies,

        ---------- numerics


        ---------- booleans
        

        ---------- dates
        

        ---------- timestamps
        created_at,
        updated_at

    from source

)

select * from renamed