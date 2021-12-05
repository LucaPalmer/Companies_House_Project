library(tidyverse)

data = read.csv('C:/Users/lucap/viz_df.csv')

data %>%
  ggplot(mapping = aes(x = accounts.accounting_reference_date_month)) +
  layer(
    stat = "bin",
        params = list(binwidth=0.5),
    geom = "bar",
    position = "identity"
  )

regions_overdue <- data %>%
  ggplot(aes(x = registered_office_address.country, fill = sic_codes))
regions_overdue +
  geom_bar()