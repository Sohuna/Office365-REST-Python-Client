from office365.entity_collection import EntityCollection
from office365.mail.itemBody import ItemBody
from office365.mail.message import Message
from office365.mail.recipient import RecipientCollection


class MessageCollection(EntityCollection):
    """Message's collection"""

    def __init__(self, context, resource_path=None):
        super(MessageCollection, self).__init__(context, Message, resource_path)

    def add(self, subject, content_html, to_emails):
        """
        Use this API to create a draft of a new message. Drafts can be created in any folder
        and optionally updated before sending. To save to the Drafts folder, use the /messages shortcut.
        :param str subject:
        :param str content_html:
        :param list[str] to_emails:
        :rtype: Message
        """

        payload = {
            "subject": subject,
            "importance": "Low",
            "body": ItemBody(content_html, "HTML"),
            "toRecipients": RecipientCollection.from_emails(to_emails),
        }
        return self.add_from_json(payload)

    def get(self):
        """
        :rtype: MessageCollection
        """
        return super(MessageCollection, self).get()
