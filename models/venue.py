class Venue:
    def __init__(
        self,
        title,
        address,
        delivery_price,
        status,
        score,
        price_range,
        location,
        estimate,
        slug,
    ):
        self.title = title
        self.address = address
        self.delivery_price = delivery_price
        self.status = status
        self.score = score
        self.price_range = price_range
        self.location = location
        self.estimate = estimate
        self.slug = slug
