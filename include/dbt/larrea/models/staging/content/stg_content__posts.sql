with

source as (

    select * from {{ source('content', 'microblog') }}

),

renamed as (

    select

        ----------  ids
        id as post_id,
        ---------- strings
        post,
        ---------- numerics


        ---------- booleans
        

        ---------- dates
        

        ---------- timestamps
        created_at

    from source

)

select * from renamed