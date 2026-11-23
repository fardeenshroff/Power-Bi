let
    Source = Csv.Document(File.Contents("C:\\DATA\\sales_orders.csv"),
        [Delimiter=",", Columns=10, Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Headers = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Headers, {
        {"order_id",type text},{"order_date",type date},{"customer_id",type text},
        {"customer_name",type text},{"region",type text},{"product_id",type text},
        {"product_name",type text},{"category",type text},{"quantity",Int64.Type},
        {"unit_price",Currency.Type}}),
    AddedRevenue = Table.AddColumn(Typed,"Revenue",
        each [quantity]*[unit_price],Currency.Type),
    ValidRows = Table.SelectRows(AddedRevenue,each [quantity]>0 and [unit_price]>=0),
    DistinctOrders = Table.Distinct(ValidRows,{"order_id"})
in
    DistinctOrders
