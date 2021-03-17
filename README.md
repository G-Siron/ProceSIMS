# ProceSIMS
GUI Python application to process SIMS data.

This Python application allows to extract data from the .asc files generated by Cameca for SIMS anlayses.
It allows to evaluate if a drift correction is required for a session and can perform such fit for up to 3 standards, simultaneously, through multivariate weighted least squares.
It automatically propagate internal errors (2SE), working standard error (2SE) and uncertainty on the reference value (available when only one standard is used to correct for teh session).
