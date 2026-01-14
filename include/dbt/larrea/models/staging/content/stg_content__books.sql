with

source as (

    select * from {{ source('content', 'books') }}

),

renamed as (

    select

        ----------  ids
        id as book_id,
        isbn as isbn,

        ---------- strings
        title as book_title,
        author as book_authors,
        image as book_image,
        labels as taxonomies,

        ---------- numerics


        ---------- booleans
        

        ---------- dates
        

        ---------- timestamps
        created_at

    from source

)

select * from renamed