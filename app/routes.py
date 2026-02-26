def register_routes(api, app, root='api'): 
    from .posts import register_route as attach_posts


    attach_posts(api, app, root)
