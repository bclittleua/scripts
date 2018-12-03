# system library for getting the command line argument
import sys

# web library
import http.client

def send( message ):

    # your webhook URL
    webhookurl = "https://discordapp.com/api/webhooks/516041675496357898/rWtIENFI3aewfq0_L-kHFjXaoZOE06WQBin1Mm6GDmc7d0ffZMXaui8fr5J4_k1Iz8xt"

    # compile the form data (BOUNDARY can be anything)
    formdata = "------:::BOUNDARY:::\r\nContent-Disposition: form-data; name=\"content\"\r\n\r\n" + "SWmud has been up for " + message + "\r\n------:::BOUNDARY:::--"

    # get the connection and make the request
    connection = http.client.HTTPSConnection("discordapp.com")
    connection.request("POST", webhookurl, formdata, {
        'content-type': "multipart/form-data; boundary=----:::BOUNDARY:::",
        'cache-control': "no-cache",
        })

    # get the response
    response = connection.getresponse()
    result = response.read()

    # return back to the calling function with the result
    return result.decode("utf-8")



# send the messsage and print the response
print( send( sys.argv[1] ) )
