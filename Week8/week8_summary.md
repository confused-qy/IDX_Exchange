# Week 8 Summary - Tableau Market Analysis Workbook

## 1. Goal

Week 8 focused on moving from cleaned analytical CSV outputs into Tableau dashboard development. The main deliverable was the first completed version of the Tableau workbook:

- `market_analysis.twbx`

The workbook was built using the cleaned, Residential-filtered Week 7 datasets and was uploaded to Tableau Public for review and sharing.

## 2. Input Data

The Tableau workbook uses the Week 7 clean filtered datasets:

- `week7_output/Sold_Week7_Clean_Filtered.csv`
- `week7_output/Listed_Week7_Clean_Filtered.csv`

These files were selected because they already:

- Keep only Residential records.
- Remove invalid numeric records.
- Remove IQR outliers from key analytical fields.
- Preserve geographic and property subtype fields needed for dashboard filters.
- Include monthly data from January 2024 through the latest available month, April 2026.

## 3. Tableau Data Source Usage

The sold and listed files were used for different analytical purposes.

### Sold Dataset

`Sold_Week7_Clean_Filtered.csv` was used for closed-sale metrics:

- Monthly median close price
- Average days on market
- Average close-to-original-list price ratio
- Closed sales
- Price-per-square-foot analysis
- Market strength comparisons by geography and property subtype

Key fields:

- `close_date`
- `close_price`
- `days_on_market`
- `close_to_original_list_ratio`
- `price_per_sqft`
- `listing_key`
- `city`
- `county_or_parish`
- `postal_code`
- `property_sub_type`

### Listed Dataset

`Listed_Week7_Clean_Filtered.csv` was used for listing-side metrics:

- New listings
- Listing activity by month
- Listing-side geographic and property subtype comparisons

Key fields:

- `listing_contract_date`
- `list_price`
- `listing_key`
- `city`
- `county_or_parish`
- `postal_code`
- `property_sub_type`

## 4. Required Dashboard Coverage

The workbook includes the required market trend dashboards.

### Monthly Median Close Price

Data source:

- Sold dataset

Main fields:

- Month: `close_date`
- Metric: `MEDIAN(close_price)`

Purpose:

- Shows monthly price trends for closed Residential sales.
- Supports filtering by geography and property subtype.

### Average Days on Market

Data source:

- Sold dataset

Main fields:

- Month: `close_date`
- Metric: `AVG(days_on_market)`

Purpose:

- Measures how quickly homes are selling over time.
- Helps identify faster or slower market periods.

### Average Close-to-Original-List Price Ratio

Data source:

- Sold dataset

Main fields:

- Month: `close_date`
- Metric: `AVG(close_to_original_list_ratio)`

Purpose:

- Measures pricing strength relative to the original list price.
- Helps identify whether homes are generally selling above, near, or below original asking price.

### New Listings

Data source:

- Listed dataset

Main fields:

- Month: `listing_contract_date`
- Metric: `COUNTD(listing_key)`

Purpose:

- Shows monthly new listing supply.
- Uses listing contract date rather than close date because this is a listing-side metric.

### Closed Sales

Data source:

- Sold dataset

Main fields:

- Month: `close_date`
- Metric: `COUNTD(listing_key)`

Purpose:

- Shows monthly completed sales volume.
- Supports comparison against new listing activity.

## 5. Filters Added

The dashboards were designed to support required market filtering.

Primary filters:

- `city`
- `county_or_parish`
- `postal_code`
- `property_sub_type`

The sold and listed datasets both contain these fields, but they represent different event pools. Sold data represents closed transactions, while listed data represents new listing activity. Because of this, listing-side and sold-side charts may show different distributions even when using the same property subtype filter.

## 6. Additional Market Analysis Dashboard

In addition to the required dashboards, the workbook includes a custom market analysis dashboard designed to compare market strength across segments.

The custom dashboard focuses on market performance indicators such as:

- Closed sales volume
- Median close price
- Average days on market
- Average close-to-original-list price ratio
- Price per square foot
- Geographic differences by city, county, or ZIP code
- Property subtype differences

This dashboard helps answer which areas or property subtypes are showing stronger demand, faster sales, or higher pricing power.

## 7. Tableau Public Upload

The `market_analysis.twbx` workbook was uploaded to Tableau Public after the main dashboard build was completed.

This makes the workbook easier to review and share without requiring local Tableau Desktop access. The Tableau Public version can be used for feedback before final Weeks 9-10 refinements.


