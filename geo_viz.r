# library(tidyverse) requires dplyr, ggplot2, tidyr
library(dplyr)
library(ggplot2)
library(tidyr)
library(ggmosaic)

data = read.csv('/home/luca/Documents/viz_df.csv')

acc_ref <- data %>%
  arrange(accounts.accounting_reference_date_month)

acc_ref %>%
  ggplot(mapping = aes(x = data$accounts.accounting_reference_date_month, fill="wheat2", show.legend = FALSE)) +
  layer(
    stat = "count",
    params = list(binwidth= 1),
    geom = "bar",
    position = "identity"
  ) +
  scale_x_continuous(breaks = c(01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12)) + 
  #scale_fill_discrete(labels = c("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Sep", "Oct", "Nov", "Dec")) +
  labs(title = "Sum of Accounts with Monthly Accounting Reference", x = "Months", y = "Account Quantity") + 
  guides(fill = "none") + 
  theme_classic()

# Visualisation below has empty country values omitted

regions_overdue <- data[!(data$registered_office_address.country == ""), ] %>%
  ggplot(aes(x = registered_office_address.country, fill = accounts.last_accounts_type))
regions_overdue +
  guides(fill=guide_legend(title = NULL)) + 
  scale_fill_discrete(labels = c("Audit Exemption Subsidiary", "Audited Abridged", "Dormant", "Full", "Group",
                                 "Micro-Entity", "NULL", "Small", "Total Exemption Full",
                                 "Total Exemption Small", "Unaudited Abridged")) +
  labs(title = "Account Types by Country", x = "Country", y = "Account Quantity") + 
  geom_bar()

regions_overdue <- data[!(data$registered_office_address.country == ""), ] %>%
  ggplot(aes(x = registered_office_address.country, fill = company_status))
regions_overdue +
  guides(fill=guide_legend(title = NULL)) + 
  scale_fill_discrete(labels = c("Active", "Dissolved", "Liquidation", "Receivership")) +
  labs(title = "Company Status by Country", x = "Country", y = "Account Quantity") + 
  geom_bar()


regions_overdue <- data[!(data$registered_office_address.country == ""), ] %>%
  ggplot(aes(x = registered_office_address.country, fill = company_status))
regions_overdue +
  geom_histogram(fill = "cornflowerblue",
                 color = "white",
                 stat= "count") +
  facet_wrap(~has_charges, ncol = 1) +
  labs(title = "Accounts with(1) or without (0) Charges by Country",
       x = "Countries", y = "Account Quantity")

regions_overdue <- data[!(data$registered_office_address.country == ""), ] %>%
  ggplot(aes(x = registered_office_address.country, fill = company_status))
regions_overdue +
  geom_histogram(fill = "red",
                 color = "white",
                 stat= "count") +
  facet_wrap(~accounts.overdue, ncol = 1) +
  labs(title = "Accounts Overdue (1) or Not Overdue (0) by Country",
       x = "Countries", y = "Account Quantity")

"""
regions_overdue <- data[!(data$registered_office_address.country == ""), ] %>%
  ggplot(aes(data = data))
regions_overdue +
  geom_mosaic(aes(x = product(company_status), fill = company_status), divider='hspine') +
  labs(y = "", title='Distribution of Company Statuses based on Region') +
  facet_grid(~registered_office_address.country) +
  theme(axis.text.y=element_blank(),
        axis.ticks.y=element_blank(),
        axis.text.x = element_text(angle = 90))
  
regions_overdue <- data[!(data$registered_office_address.country == ""), ] %>%
  ggplot(aes(data = data))
regions_overdue +
  geom_mosaic(aes(x = product(company_status), fill = company_status), divider='hbar') +
  facet_grid(~registered_office_address.country) +
  theme_mosaic()
"""


data$date_of_creation <- ymd(data$date_of_creation)
ggplot(data, aes(x=date_of_creation, y=can_file)) +
  geom_line() +
  xlab("") +
  scale_x_date(limit=c(as.Date("1970-02-16"), as.Date("2021-11-18")))
