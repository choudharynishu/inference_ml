from pydantic import BaseModel


class FMCG(BaseModel):
    """
    FMCG data schema.

    Date - Date for which the data was recorded
    Product Category -
    Price - Price of the particular product
    Promotion - Binary, if any promotion is going on
    Store_Location - Location of the store, Urban, Rural, or Suburban
    Weekday - Day of the week, value varies from 0-6
    Supplier_cost - Procurement cost of the good
    Replenishment_Lead_Time - Total time to replenish stock
    Stock_level - Current stock level of the item
    """

    Product_Category: int
    Price: float
    Promotion: int
    Store_Location: int
    Weekday: int
    Supplier_Cost: float
    Replenishment_Lead_Time: int
    Stock_level: int
