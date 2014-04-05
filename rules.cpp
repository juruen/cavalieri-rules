#include <rules.h>
#include <external/pagerduty.h>
#include <external/email.h>

streams_t* rules() {

  auto mail_stream = email("localhost", "cavalieri@localhost",
                           "devops@localhost");

  auto s =  where(service_pred("requests_rate"))
              >> above(40)
                >> with({{"state", "critical"}})
                  >> changed_state("ok")
                    >>  mail_stream;

  return new streams_t(s);
}
